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
                        :item-i-d-for-edit="editItemID"
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
                        text-title="product"
                        desc="This action will permanently delete this product."
                        :item-values="deleteItemValues"
                        :items="deleteTableValues"
                        item-type="product"
                        @on-cancel="reinitializeModalVariables"
                        @on-confirm="handleSubmitFromModal"
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
                :rows="products"
                :table-state="tableState"
                item-type="product"
                table-state-text="Product list"
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

// Modules
import getAllProducts from '@/modules/product/getAllProducts';
import DeleteModal from '@/components/Modals/DeleteModal.vue';

// Variables for inits
const { products, error, load } = getAllProducts(); 
const legends = [
    { id: 'skuid', text: 'SKU ID' },
    { id: 'name', text: 'Product Name' },
    { id: 'category', text: 'Category' },
    { id: 'price', text: 'Price' },
    { id: 'actions', text: 'Actions' },
];
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
const tableState = ref('loading'); // default this to loading
const successfulMessage = ref('');
const editItemID = ref(null);
const deleteItemValues = ref({});
const modalModelValues = reactive({
    sku: '',
    name: '',
    category: '',
    price: '',
});
const deleteTableValues = ref([
    { legend: 'SKUID', value: '' },
    { legend: 'Product Name', value: '' },
    { legend: 'Category', value: '' },
    { legend: 'Price', value: '' }
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

    deleteTableValues.value.forEach(item => {
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
function handleTableRowEdit(rowIndex) {
    const product = products.value[rowIndex];
    
    activeTableRow.value = rowIndex;
    isOverlayCalled.value = true;
    modalType.value = 'edit';
    editItemID.value = product.id;

    modalModelValues.sku = product.sku;
    modalModelValues.name = product.name;
    modalModelValues.category = product.category;
    modalModelValues.price = product.price;

    console.log(modalModelValues);

    // use for debug
    // console.log('==============')
    // console.log('modalModelValues: ');
    // console.log(modalModelValues.value);
};

// Opens the modal for delete
function handleTableRowDelete(rowIndex) {
    const product = products.value[rowIndex];
    console.log(products.value);
    
    deleteItemValues.value = product;
    activeTableRow.value = rowIndex;
    isOverlayCalled.value = true;
    modalType.value = 'delete';

    const productValues = [
        product.sku,
        product.name,
        product.category,
        product.price,
    ]
    
    deleteTableValues.value.forEach((item, index) => {
        item.value = productValues[index];
    });
};

// Handle successful add/edit submission from modal
function handleSubmitFromModal(submittedValues, hasNoChangesOnEdit = false) {
    const item = submittedValues.name;

    const messageTemplates = {
        add: `${ item } has been added successfully!`,
        edit: `${ item } has been updated successfully!`,
        delete: `${ item } has been removed successfully!`,
    };

    if (hasNoChangesOnEdit) messageIcon.value = 'noChangesIcon';
    else messageIcon.value = `${ modalType.value }Icon`;

    successfulMessage.value = messageTemplates[modalType.value];
    modalType.value = 'message';
    products.value = [];

    loadItems();
};

// Function reusables
async function loadItems() {
    tableState.value = 'loading';

    await load();
    console.log(products.value);
        
    if (error.value === null) {
        const productLength = products.value.length
        
        tableState.value = productLength === 0 ? 'empty' : 'exist';
    } else {
        tableState.value = 'empty';
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