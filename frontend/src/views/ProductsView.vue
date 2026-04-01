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
                        text-title="product"
                        desc="This action will permanently delete this product."
                        item-type="product"
                        @on-cancel=""
                        @on-confirm=""
                    />
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
                                id="addIcon"
                                size="18"
                                :color="btnAddIconColor"
                            />
                        </template>
                    </PrimaryButton>
                </div>
            </section>
            <SimpleTable 
                table-is-used-as="products"
                :legends="tableLegends"
                :rows="tableRows"
                :table-state="tableState"
                :table-state-texts="tableStateTexts"
                @row-on-click="handleTableRowOnClick"
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
import getAllProducts from '@/modules/product/getAllProducts';

// Use Modules
import Templates from '@/modules/utils/useTemplates';

// Personal Variables
const { products, error, load } = getAllProducts();
const { tableRowTemplates } = Templates();
const activeTableRow = ref(null);

// Variables for Table
const tableState = ref('default');
const tableRows = ref([]);
const tableLegends = [ // See SimpleTable.vue for template
    'Product SKU',
    'Product Name',
    'Category',
    'Price',
    'Actions'
];
const tableStateTexts = {
    loading: 'Loading items from the server...',
    offline: 'It seems that you are offline...',
    empty: 'Products seem to be empty...' 
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
    { type: 'text', hint: 'Product Name' },
    { type: 'dropdowntext', hint: 'Category' },
    { type: 'text', hint: 'Price' },
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
    modalTitle.value = 'Add new product';
};

// Functions Reusable
async function loadItems() {
    tableState.value = 'loading';
    await load();

    if (error.value === null && products.value.length !== 0) {
        products.value.forEach((product, rowIndex) => {
            // product is an object containing a product's data

            let newTableRow = tableRowTemplates(
                'product', 
                rowIndex,
                product
            );

            tableRows.value.push(newTableRow);
            tableState.value = 'default';
        });
    } else {
        tableState.value = 'empty';
    };
};

// // Variables for inits
// const { products, error, load } = getAllProducts(); 
// const legends = [
//     { id: 'skuid', text: 'SKU ID' },
//     { id: 'name', text: 'Product Name' },
//     { id: 'category', text: 'Category' },
//     { id: 'price', text: 'Price' },
//     { id: 'actions', text: 'Actions' },
// ];
// // Do see the SimpleAddEditModal.vue for field object
// const modalAddEditFields = [ // Change this later to inventory
//     { id: 1, type: 'text',  hintText: 'SKU ID*' },
//     { id: 2, type: 'text',  hintText: 'Product Name*' },
//     { id: 3, type: 'dropdowntext',  hintText: 'Category*' },
//     { id: 4, type: 'text',  hintText: 'Price*' },
// ];
    

// // Variables for Child
// const messageIcon = ref(null); // addIcon, editIcon, deleteIcon, messageIcon
// const modalType = ref(null); // add, edit, delete, message
// const isOverlayCalled = ref(false);
// const activeTableRow = ref(null);
// const tableState = ref('loading'); // default this to loading
// const successfulMessage = ref('');
// const editItemID = ref(null);
// const deleteItemValues = ref({});
// const modalModelValues = reactive({
//     sku: '',
//     name: '',
//     category: '',
//     price: '',
// });
// const deleteTableValues = ref([
//     { legend: 'SKUID', value: '' },
//     { legend: 'Product Name', value: '' },
//     { legend: 'Category', value: '' },
//     { legend: 'Price', value: '' }
// ]);

// // Load data after mount
// onMounted(() => {
//     loadItems();
// });

// // Variables for children
// const btnAddIconColor = ref("#FFFAFA");

// // Function Appearances
// function changeButtonAddIconColor() {
//     btnAddIconColor.value = btnAddIconColor.value === '#FFFAFA' ? '#C84A46' : '#FFFAFA';
// };

// function reinitializeModalVariables() {
//     isOverlayCalled.value = false;
//     successfulMessage.value = '';
//     modalType.value = null;
//     messageIcon.value = null;

//     Object.keys(modalModelValues).forEach(key => {
//         modalModelValues[key] = '';
//     });

//     deleteTableValues.value.forEach(item => {
//         item.value = '';
//     });
// };

// // Function Handlers
// // Opens the modal for edit
// function handleNewItemRequest() {
//     isOverlayCalled.value = true;
//     modalType.value = 'add'
//     activeTableRow.value = null;
// };

// // Opens the modal for edit
// function handleTableRowEdit(rowIndex) {
//     const product = products.value[rowIndex];
    
//     activeTableRow.value = rowIndex;
//     isOverlayCalled.value = true;
//     modalType.value = 'edit';
//     editItemID.value = product.id;

//     modalModelValues.sku = product.sku;
//     modalModelValues.name = product.name;
//     modalModelValues.category = product.category;
//     modalModelValues.price = product.price;

//     console.log(modalModelValues);

//     // use for debug
//     // console.log('==============')
//     // console.log('modalModelValues: ');
//     // console.log(modalModelValues.value);
// };

// // Opens the modal for delete
// function handleTableRowDelete(rowIndex) {
//     const product = products.value[rowIndex];
//     console.log(products.value);
    
//     deleteItemValues.value = product;
//     activeTableRow.value = rowIndex;
//     isOverlayCalled.value = true;
//     modalType.value = 'delete';

//     const productValues = [
//         product.sku,
//         product.name,
//         product.category,
//         product.price,
//     ]
    
//     deleteTableValues.value.forEach((item, index) => {
//         item.value = productValues[index];
//     });
// };

// // Handle successful add/edit submission from modal
// function handleSubmitFromModal(submittedValues, hasNoChangesOnEdit = false) {
//     const item = submittedValues.name;

//     const messageTemplates = {
//         add: `${ item } has been added successfully!`,
//         edit: `${ item } has been updated successfully!`,
//         delete: `${ item } has been removed successfully!`,
//     };

//     if (hasNoChangesOnEdit) messageIcon.value = 'noChangesIcon';
//     else messageIcon.value = `${ modalType.value }Icon`;

//     successfulMessage.value = messageTemplates[modalType.value];
//     modalType.value = 'message';
//     products.value = [];

//     loadItems();
// };

// // Function reusables
// async function loadItems() {
//     tableState.value = 'loading';

//     await load();
//     console.log(products.value);
        
//     if (error.value === null) {
//         const productLength = products.value.length
        
//         tableState.value = productLength === 0 ? 'empty' : 'exist';
//     } else {
//         tableState.value = 'empty';
//     };
// };
</script>

<style scoped>
#products {
    width: 100%;
    position: relative;
}

#addIcon {
    transition: 0.3s
}

@import '../styles/shared-views/views.css';
</style>