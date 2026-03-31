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
                :rows="rows"
                :table-state="tableState"
                table-state-text="Inventory"
                @on-row-edit="handleTableRowEdit"
                @on-row-delete=""
                @on-empty-add="handleNewItemRequest"
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

// Variables for inits
const { inventory, error, load } = getAllInventory();
const inventoryData = ref(null);
const legends = [
    { id: 'skuid', text: 'SKU ID' },
    { id: 'name', text: 'Product Name' },
    { id: 'category', text: 'Category' },
    { id: 'price', text: 'Price' },
    { id: 'actions', text: 'Actions' },
];
const rows = ref([]); // Used for table rows
// Do see the SimpleAddEditModal.vue for field object
const modalAddEditFields = [ // Change this later to inventory
    { id: 1, type: 'text',  hintText: 'Product ID' },
    { id: 2, type: 'text',  hintText: 'Description' },
    { id: 3, type: 'text',  hintText: 'Quantity' },
];

// Variables for Child
const messageIcon = ref(null); // addIcon, editIcon, deleteIcon, messageIcon
const modalType = ref(null); // add, edit, delete, message
const isOverlayCalled = ref(false);
const activeTableRow = ref(null);
const successfulMessage = ref('');
const tableState = ref('loading'); // default this to null
const modalModelValues = ref([
    { id: 1, value: '' },
    { id: 2, value: '' },
    { id: 3, value: '' },
    { id: 4, value: '' },
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
    modalType.value = null;
    isOverlayCalled.value = false;
    successfulMessage.value = '';
    messageIcon.value = null;

    modalModelValues.value.forEach(item => {
        item.value = '';
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
function handleTableRowEdit(rowID) {
    const row = rows.value[rowID];
    
    activeTableRow.value = rowID;
    isOverlayCalled.value = true;
    modalType.value = 'edit';
    
    modalModelValues.value.forEach((item, index) => {
        item.value = row[index];
    });
};

function handleTableRowDelete(rowID) {
    const row = rows.value[rowID];

    activeTableRow.value = rowID;
    isOverlayCalled.value = true;
    modalType.value = 'delete';
};

// Handle successful add/edit submission from modal
async function handleSubmitFromModal(item, hasNoChangesOnEdit) {
    const messageTemplates = {
        add: `${ item.name } has been added successfully!`,
        edit: `${ item.name } has been updated successfully!`,
        delete: `${ item.name } has been removed successfully!`,
    };

    if (hasNoChangesOnEdit) messageIcon.value = 'noChangesIcon';
    else messageIcon.value = `${ modalType.value }Icon`;

    rows.value = [];
    successfulMessage.value = messageTemplates[modalType.value];
    modalType.value = 'message';

    loadItems();
};

// Function reusables
async function loadItems() {
    tableState.value = 'loading';

    await load();
        
    if (error.value === null) {
        // Change all this later
        inventoryData.value = inventory.value;
        // use for debug
        // console.log('==============')
        // console.log('inventoryData: ');
        // console.log(inventoryData.value);

        // Iterates over the given array
        inventoryData.value.forEach(data => {
            let newItem = [];

            /*
            * Get all values from the data
            * value here refers to the data
            * from the server. For example:
            * for inventory, we have quantity
            * and value gives the value of quantity
            * say 5.
            */
            Object.values(data).forEach(value => {
                newItem.push(value);
            });

            rows.value.push(newItem); // Add values as rows
        });

        const rowsLength = rows.value.length

        tableState.value = rowsLength === 0 ? 'empty' : 'exist';

        // use for debug
        // console.log('==============')
        // console.log('inventoryData: ');
        // console.log(rows.value); 
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