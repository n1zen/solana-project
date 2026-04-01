<template>
    <transition name="fade">
        <Overlay
            v-if="isOverlayCalled"
            @on-click="handleCloseModalRequest"
            >
            <template #sSurface>
                <transition name="fade" mode="out-in">
                    <SimpleAddEditModal 
                        v-if="
                        modalType === 'add' ||
                        modalType === 'edit'
                        "
                        modal-return-text="Cancel"
                        :modal-title="modalTitle"
                        :modal-missing-input-text="modalMissingInputText"
                        :input-fields="modalInputFields"
                        :input-values="modalInputValues"
                        :item-row-i-d="activeTableRow"
                        @on-cancel="handleCloseModalRequest"
                        @on-submit=""
                    />
                    <MessageModal 
                        v-else-if="modalType === 'message'"
                        :message="''"
                        @on-confirm=""
                        >
                        <template #sMessageIcon>
                            <PackagePlus 
                                v-if="messageIcon === 'addIcon'"
                                size="60"
                                color="var(--color-valid)"
                                />
                            <PackageCheck 
                                v-if="messageIcon === 'editIcon'"
                                size="60"
                                color="var(--color-valid)"
                                />
                            <PackageX 
                                v-if="messageIcon === 'deleteIcon'"
                                size="60"
                                color="var(--color-valid)"
                                />
                            <FilePen 
                                v-if="messageIcon === 'noChangesIcon'"
                                size="60"
                                color="var(--color-valid)"
                            />
                        </template>
                    </MessageModal>
                    <DeleteModal 
                        v-else-if="modalType === 'delete'"
                        text-title="inventory"
                        desc="This action will permanently delete this item."
                        item-type="inventory"
                        @on-cancel=""
                        @on-confirm=""
                    />
                </transition>
            </template>
        </Overlay>
    </transition>
    <div class="page" id="page-inventory">
        <div id="inventory">
            <section id="header">
                <h1>Product Inventory</h1>
                <div id="actions">
                    <PrimaryButton 
                        text="New Product" 
                        :has-icon="true"
                        @on-hover="changeButtonAddIconColor"
                        @on-leave="changeButtonAddIconColor"
                        @on-click="handleNewItemRequest"
                    >
                        <template #sIcon>
                            <Plus 
                                id="addIcon"
                                size="18"
                                :color="btnAddIconColor"
                            />
                        </template>
                    </PrimaryButton>
                </div>
            </section>
            <SimpleTable 
                table-is-used-as="inventory"
                :legends="tableLegends"
                :rows="tableRows"
                :table-state="tableState"
                :table-state-texts="tableStateTexts"
            />
        </div>
    </div>
</template>

<script setup>
// Imports outside
import { FilePen, PackageCheck, PackagePlus, PackageX, Plus } from 'lucide-vue-next';

// Vue
import { onMounted, reactive, ref } from 'vue';

// Components
import PrimaryButton from '@/components/Buttons/PrimaryButton.vue';
import SimpleTable from '@/components/Tables/SimpleTable/SimpleTable.vue';
import Overlay from '@/components/Modals/Overlay.vue';
import MessageModal from '@/components/Modals/MessageModal.vue';
import SimpleAddEditModal from '@/components/Modals/SimpleAddEditModal.vue';
import DeleteModal from '@/components/Modals/DeleteModal.vue';

// Modules
import getAllInventory from '@/modules/inventory/getAllInventory';

// Use Modules
import Templates from '@/modules/utils/useTemplates';

const { inventory, error, load } = getAllInventory();
const { tableRowTemplates } = Templates();
const activeTableRow = ref(null);

// Variables for Table
const tableState = ref('default');
const tableRows = ref([]);
const tableLegends = [ // See SimpleTable.vue for template
    'Product SKU',
    'Product Name',
    'Quantity',
    'Actions'
];
const tableStateTexts = {
    loading: 'Loading items from the server...',
    offline: 'It seems that you are offline...',
    empty: 'Inventory seems to be empty...' 
}

// Variables for Child
// New Primary Button
const btnAddIconColor = ref('var(--color-primary)');

// Overlays
const isOverlayCalled = ref(false);

// Modals
const modalType = ref('');
const modalTitle = ref('');
const modalMissingInputText = ref('');
const modalInputFields = ref([
    { type: 'text', hint: 'Product SKU' },
    { type: 'dropdowntext', hint: 'Product Name' },
    { type: 'text', hint: 'Details' },
    { type: 'text', hint: 'Quantity' },
]);
const modalInputValues = ref({
    sku: '',
    name: '',
    category: '',
    price: ''
});

// Initialize
onMounted(() => {
    loadItems();
});

// Function for Child
// New Primary Button
function changeButtonAddIconColor(isHovered) {
    btnAddIconColor.value = isHovered ? 
        'var(--color-secondary)' :
        'var(--color-primary)';
};

// Simple Table
function handleTableRowOnClick(rowIndex) {
    activeTableRow.value = rowIndex;
};

// Function Handlers
function handleCloseModalRequest() {
    isOverlayCalled.value = false;
    modalType.value = '';
    modalTitle.value = '';
};

function handleNewItemRequest() {
    isOverlayCalled.value = true;
    modalType.value = 'add';
    modalTitle.value = 'Add new item';
};

// Functions Reusable
async function loadItems() {
    tableState.value = 'loading';
    await load();

    if (error.value === null && inventory.value.length !== 0) {
        inventory.value.forEach((item, rowIndex) => {
            // inventory is an object containing a inventory's data

            let newTableRow = tableRowTemplates(
                'inventory',
                rowIndex,
                item
            );

            tableRows.value.push(newTableRow);
            tableState.value = 'default';
        });
    } else {
        tableState.value = 'empty';
        console.log('ahsdkajsd');
    };
};

</script>

<style scoped>
#inventory {
    width: 100%;
    position: relative;
}

@import '../styles/shared-views/views.css';
</style>