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
                        :item-type="0"
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
                        item-type="product"
                        :table-values="deleteModalTableValues"
                        :item-i-d="modalItemID"
                        @on-cancel="handleCloseModalRequest"
                        @on-confirm="handleOnSubmitSuccess"
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
import getAllProducts from '@/modules/product/getAllProducts';

// Use Modules
import Templates from '@/modules/utils/useTemplates';

// Personal Variables
const { products, error, load } = getAllProducts();
const { tableRowTemplates, messageTemplates } = Templates();
const activeTableRow = ref(null);
const wasModalAddType = ref(false);

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
const modalItemID = ref('');
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

// Delete Modal
const deleteModalTableValues = ref({
    sku: { legend: 'Product SKU', value: '' },
    name: { legend: 'Product Name', value: '' },
    category: { legend: 'Category', value: '' },
    price: { legend: 'Price', value: '' },
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
    
    Object.keys(modalInputValues.value).forEach(key => {
        modalInputValues.value[key] = '';
    });

    Object.keys(deleteModalTableValues.value).forEach(key => {
        deleteModalTableValues.value[key].value = '';
    });

    loadItems();
};

function handleNewItemRequest() {
    isOverlayCalled.value = true;
    modalType.value = 'add';
    modalTitle.value = 'Add new product';
};

function handleOnEditItemRequest(rowIndex) {
    const tableRowToEdit = tableRows.value[rowIndex];

    Object.keys(modalInputValues.value).forEach(key => {
        modalInputValues.value[key] = tableRowToEdit[key];
    });

    isOverlayCalled.value = true;
    modalType.value = 'edit';
    modalTitle.value = `Edit Product ${ modalInputValues.value.sku }?`;
    modalItemID.value = tableRowToEdit.id;
};

function handleOnDeleteItemRequest(rowIndex) {
    const tableRowToDelete = tableRows.value[rowIndex];

    Object.keys(deleteModalTableValues.value).forEach(key => {
        deleteModalTableValues.value[key].value = tableRowToDelete[key]; 
    });

    isOverlayCalled.value = true;
    modalType.value = 'delete';
    modalTitle.value = `Delete Product ${ deleteModalTableValues.value.sku.value }?`;
    modalItemID.value = tableRowToDelete.id;
};

function handleOnSubmitSuccess(submittedValues, noChanges = false) {
    
    messageModalMessage.value = messageTemplates(
        'product',
        modalType.value,
        submittedValues,
        'sku'
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
#products {
    width: 100%;
    position: relative;
}

#addIcon {
    transition: 0.3s
}

@import '../styles/shared-views/views.css';
</style>