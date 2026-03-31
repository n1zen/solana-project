<template>
    <transition name="fade">
        <Overlay
            v-if="isOverlayCalled"
            @on-click="reinitializeModalVariables"
            >
            <template #sSurface>
                <transition name="fade" mode="out-in">
                    <SimpleAddEditModal 
                        v-if="
                        modalType === 'add' ||
                        modalType === 'edit'
                        "
                        :fields="modalAddEditFields"
                        :model-values="modalModelValues"
                        :modal-type="modalType"
                        :itemType="1"
                        :row-i-d-for-edit="activeTableRow"
                        @on-cancel="reinitializeModalVariables"
                        @on-submit="handleSubmitFromModal"
                    />
                    <MessageModal 
                        v-else-if="modalType === 'message'"
                        :message="successfulMessage"
                        @on-confirm="reinitializeModalVariables"
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
                        :item-i-d="deleteRowItemID"
                        :item-name="deleteItemName"
                        :items="deleteTableValues"
                        item-type="inventory"
                        @on-cancel="reinitializeModalVariables"
                        @on-confirm="handleSubmitFromModal"
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
                        text="New Inventory" 
                        :has-icon="true"
                        @on-hover="changeButtonAddIconColor"
                        @on-leave="changeButtonAddIconColor"
                        @on-click="handleNewItemRequest"
                    >
                        <template #sIcon>
                             <Plus 
                                size="18"
                                :color="btnAddIconColor"
                             />
                        </template>
                    </PrimaryButton>
                </div>
            </section>
            <SimpleTable 
                table-i-d="inventory"
                :legends="legends"
                :rows="inventory"
                :table-state="tableState"
                item-type="inventory"
                table-state-text="Inventory"
                @on-row-edit="handleTableRowEdit"
                @on-row-delete="handleTableRowDelete"
                @on-empty-add="handleNewItemRequest"
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

// Variables for inits
const { inventory, error, load } = getAllInventory();
const legends = [
    { id: 'product-id', text: 'Product SKU' },
    { id: 'name', text: 'Product Name' },
    { id: 'quantity', text: 'Quantity' },
    { id: 'actions', text: 'Actions' },
];
// Do see the SimpleAddEditModal.vue for field object
const modalAddEditFields = [ // Change this later to inventory
    { id: 1, type: 'dropdowntext',  hintText: 'Product SKU' },
    { id: 3, type: 'text',  hintText: 'Description' },
    { id: 4, type: 'text',  hintText: 'Quantity' },
];

// Variables for Child
const messageIcon = ref(null); // addIcon, editIcon, deleteIcon, messageIcon
const modalType = ref(null); // add, edit, delete, message
const isOverlayCalled = ref(false);
const activeTableRow = ref(null);
const successfulMessage = ref('');
const deleteRowItemID = ref(null);
const deleteItemName = ref(null);
const tableState = ref('loading'); // default this to null
const modalModelValues = reactive({
    product_id: '',
    details: '',
    quantity: '',
});
const deleteTableValues = ref([
    { legend: 'Product SKU', value: '' },
    { legend: 'Product Name', value: '' },
    { legend: 'Quantity', value: '' }
]);

// Load data after mount
onMounted(() => {
    loadItems();
});

// Variables for children
const btnAddIconColor = ref("#FFFAFA");

// Function Appearances
function changeButtonAddIconColor() {
    btnAddIconColor.value = btnAddIconColor.value === '#FFFAFA' ? '#C84A46' : '#FFFAFA';
};

function reinitializeModalVariables() {
    isOverlayCalled.value = false;
    successfulMessage.value = '';
    modalType.value = null;
    messageIcon.value = null;

    Object.keys(modalModelValues).forEach(key => {
        modalModelValues[key] = '';
    });
};

// Function Handlers
// Opens the modal for edit
function handleNewItemRequest() {
    isOverlayCalled.value = true;
    modalType.value = 'add'
    activeTableRow.value = null;
};

// Opens the modal for edit
function handleTableRowEdit(rowIndex) {
    const inventoryItem = inventory.value[rowIndex];
    
    activeTableRow.value = rowIndex;
    isOverlayCalled.value = true;
    modalType.value = 'edit';

    modalModelValues.product_id = inventoryItem.product?.sku;
    modalModelValues.details = inventoryItem.details;
    modalModelValues.quantity = inventoryItem.quantity;
    
    // use for debug
    // console.log('==============')
    // console.log('modalModelValues: ');
    // console.log(modalModelValues.value);
};

function handleTableRowDelete(rowItemID, rowIndex) {
    const inventoryItem = inventory.value[rowIndex];
    
    deleteRowItemID.value = rowItemID;
    activeTableRow.value = rowIndex;
    isOverlayCalled.value = true;
    modalType.value = 'delete';

    const itemValues = [
        inventoryItem.id,
        inventoryItem.product?.name,
        inventoryItem.quantity,
    ]
    
    deleteTableValues.value.forEach((item, index) => {
        item.value = itemValues[index];
    });

    deleteItemName.value = itemValues[1];
};

// Handle successful add/edit submission from modal
async function handleSubmitFromModal(hasNoChangesOnEdit = false) {
    const item = inventory.value[activeTableRow.value];
    const itemName = item.product?.name

    const messageTemplates = {
        add: `${ itemName } has been added successfully!`,
        edit: `${ itemName } has been updated successfully!`,
        delete: `${ itemName } has been removed successfully!`,
    };

    console.log(item);

    if (hasNoChangesOnEdit) messageIcon.value = 'noChangesIcon';
    else messageIcon.value = `${ modalType.value }Icon`;

    successfulMessage.value = messageTemplates[modalType.value];
    modalType.value = 'message';

    loadItems();
};

// Function reusables
async function loadItems() {
    tableState.value = 'loading';

    await load();

    if (error.value === null) {
        const inventoryLength = inventory.value.length
        
        tableState.value = inventoryLength === 0 ? 'empty' : 'exist';
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