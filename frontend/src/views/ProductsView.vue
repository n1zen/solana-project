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
                        :itemType="0"
                        :row-i-d-for-edit="activeTableRow"
                        @on-cancel="reinitializeModalVariables"
                        @on-submit="handleSubmitFromModal"
                    />
                    <MessageModal 
                        v-else-if="modalType === 'message'"
                        :message="successfulMessage"
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
                </transition>
            </template>
        </Overlay>
    </transition>
    <div class="page" id="page-products">
        <div id="products">
            <section id="header">
                <h1>Product List</h1>
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
                                size="18"
                                :color="btnAddIconColor"
                             />
                        </template>
                    </PrimaryButton>
                </div>
            </section>
            <SimpleTable 
                table-i-d="product"
                :legends="legends"
                :rows="rows"
                @on-row-edit="handleTableRowEdit"
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
import SimpleAddEditModal from '@/components/Modals/SimpleAddEditModal.vue';

// Modules
import getAllProducts from '@/modules/product/getAllProducts';
import MessageModal from '@/components/Modals/MessageModal.vue';

// Variables for inits
const { products, error, load } = getAllProducts(); 
const productData = ref(null);
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
    { id: 1, type: 'text',  hintText: 'SKU ID*' },
    { id: 2, type: 'text',  hintText: 'Product Name*' },
    { id: 3, type: 'dropdowntext',  hintText: 'Category*' },
    { id: 4, type: 'text',  hintText: 'Price*' },
];

// Variables for Child
const messageIcon = ref(null); // addIcon, editIcon, deleteIcon, messageIcon
const modalType = ref(null); // add, edit, delete, message
const isOverlayCalled = ref(false);
const activeTableRow = ref(null);
const successfulMessage = ref('');
const modalModelValues = ref([
    { id: 1, value: '' },
    { id: 2, value: '' },
    { id: 3, value: '' },
    { id: 4, value: '' },
]);

// Load data after mount
onMounted(async () => {
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
    await load();
        
    if (error.value === null) {
        // Change all this later
        productData.value = products.value;
        // use for debug
        // console.log('==============')
        // console.log('productData: ');
        // console.log(productData.value);

        // Iterates over the given array
        productData.value.forEach(data => {
            let newItem = [];

            /*
            * Get all values from the data
            * value here refers to the data
            * from the server. For example:
            * for products, we have price
            * and value gives the value of price
            * say 150.
            */
            Object.values(data).forEach(value => {
                newItem.push(value);
            });

            rows.value.push(newItem); // Add values as rows
        });

        // use for debug
        // console.log('==============')
        // console.log('productData: ');
        // console.log(rows.value); 
    } else {
        // If possible, add a catcher
    };
};
</script>

<style scoped>
#products {
    width: 100%;
    position: relative;
}

@import '../styles/shared-views/views.css';
</style>