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
                        :modal-type="modalType"
                        :modal-title="modalTitle"
                        :modal-missing-input-text="modalMissingInputText"
                        :input-fields="modalInputFields"
                        :input-values="modalInputValues"
                        :item-row-i-d="activeTableRow"
                        :item-i-d="modalItemID"
                        :item-row-index="activeTableRow"
                        item-type="inventory"
                        :search-for="searchFor"
                        @on-cancel="handleCloseModalRequest"
                        @on-submit="handleOnSubmitSuccess"
                    />
                    <MessageModal 
                        v-else-if="modalType === 'message'"
                        :message="messageModalMessage"
                        @on-confirm="handleCloseModalRequest"
                        >
                        <template #sMessageIcon>
                            <PackagePlus 
                                v-if="messageModalIcon === 'addIcon'"
                                size="60"
                                color="var(--color-valid)"
                                />
                            <PackageCheck 
                                v-if="messageModalIcon === 'editIcon'"
                                size="60"
                                color="var(--color-valid)"
                                />
                            <PackageX 
                                v-if="messageModalIcon === 'deleteIcon'"
                                size="60"
                                color="var(--color-valid)"
                                />
                            <FilePen 
                                v-if="messageModalIcon === 'noChangesIcon'"
                                size="60"
                                color="var(--color-valid)"
                            />
                        </template>
                    </MessageModal>
                    <DeleteModal 
                        v-else-if="modalType === 'delete'"
                        :modal-title="modalTitle"
                        item-type="inventory"
                        :table-values="deleteModalTableValues"
                        :item-i-d="modalItemID"
                        :item-row-index="activeTableRow"
                        @on-cancel="handleCloseModalRequest"
                        @on-confirm="handleOnSubmitSuccess"
                    />
                </transition>
            </template>
        </Overlay>
    </transition>
    <div class="page" id="page-inventory">
        <div id="inventory">
            <section id="header">
                <h1>Inventory</h1>
                <div id="actions">
                    <PrimaryButton 
                        text="New Inventory" 
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
                :clicked-row-index="activeTableRow"
                @row-on-click="handleTableRowOnClick"
                @on-empty-add-request="handleNewItemRequest"
                @on-edit-item-request="handleOnEditItemRequest"
                @on-delete-item-request="handleOnDeleteItemRequest"
            />
        </div>
    </div>
</template>

<script setup>
// Imports outside
import { FilePen, PackageCheck, PackagePlus, PackageX, Plus } from 'lucide-vue-next';

// Vue
import { onMounted, ref } from 'vue';

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
const { tableRowTemplates, messageTemplates } = Templates();
const activeTableRow = ref(null);
const wasModalAddType = ref(false);
const searchFor = ref('');

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
const modalItemID = ref('');
const modalInputFields = ref({
    product_sku: { type: 'text', linkedField: 'product_name', hint: 'Product SKU' },
    product_name: { type: 'dropdowntext', linkedField: 'product_sku', hint: 'Product Name' },
    details: { type: 'text', hint: 'Details' },
    quantity: { type: 'text', hint: 'Quantity' },
});
const modalInputValues = ref({
    product_sku: '',
    product_name: '',
    details: '',
    quantity: ''
});

// Delete Modal
const deleteModalTableValues = ref({
    product_sku: { legend: 'Product SKU', value: '' },
    product_name: { legend: 'Product Name', value: '' },
    details: { legend: 'Details', value: '' },
    quantity: { legend: 'Quantity', value: '' },
});

// Message Modal
const messageModalMessage = ref('');
const messageModalIcon = ref('');

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
    searchFor.value = '';

    Object.keys(modalInputValues.value).forEach(key => {
        modalInputValues.value[key] = '';
    });
    
    loadItems();
};

function handleNewItemRequest() {
    isOverlayCalled.value = true;
    modalType.value = 'add';
    modalTitle.value = 'Add new item';
    searchFor.value = 'product';
    activeTableRow.value = undefined;
};

function handleOnEditItemRequest(rowIndex) {
    const tableRowToEdit = tableRows.value[rowIndex];

    Object.keys(modalInputValues.value).forEach(key => {
        modalInputValues.value[key] = tableRowToEdit[key];
    });

    isOverlayCalled.value = true;
    modalType.value = 'edit';
    modalTitle.value = `Edit Product ${ modalInputValues.value.sku }`;
    modalItemID.value = tableRowToEdit.id;
    searchFor.value = 'product';
};

function handleOnDeleteItemRequest(rowIndex) {
    const tableRowToDelete = tableRows.value[rowIndex];

    Object.keys(deleteModalTableValues.value).forEach(key => {
        deleteModalTableValues.value[key].value = tableRowToDelete[key]; 
    });

    isOverlayCalled.value = true;
    modalType.value = 'delete';
    modalTitle.value = `Delete Product ${ deleteModalTableValues.value.product_sku.value }?`;
    modalItemID.value = tableRowToDelete.id;
};

function handleOnSubmitSuccess(submittedValues, noChanges = false) {
     messageModalMessage.value = messageTemplates(
        'inventory',
        modalType.value,
        submittedValues,
    );

    if (modalType.value === 'add') {
        messageModalIcon.value = 'addIcon';
        wasModalAddType.value = true;
    }
    else if (modalType.value === 'edit') messageModalIcon.value = 'editIcon';
    else if (modalType.value === 'delete') messageModalIcon.value = 'deleteIcon';
    else messageModalIcon.value = 'noChangesIcon';

    modalType.value = 'message';
};

// Functions Reusable
async function loadItems() {
    tableState.value = 'loading';
    tableRows.value = [];

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

        if (wasModalAddType.value) {
            activeTableRow.value = tableRows.value.length - 1;
            wasModalAddType.value = false;
        };
    } else {
        tableState.value = 'empty';
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