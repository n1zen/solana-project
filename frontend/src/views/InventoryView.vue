<template>
    <transition name="fade">
        <Overlay
            v-if="isOverlayCalled"
            @on-click="reinitializeModalVariables"
            >
            <template #sSurface>
                <transition name="fade">
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
                @on-row-edit="handleTableRowEdit"
            />
        </div>
    </div>
</template>

<script setup>
// Imports outside
import { Plus } from 'lucide-vue-next';

// Vue
import { onMounted, ref } from 'vue';

// Components
import PrimaryButton from '@/components/Buttons/PrimaryButton.vue';
import SimpleTable from '@/components/Tables/SimpleTable/SimpleTable.vue';
import Overlay from '@/components/Modals/Overlay.vue';
import SimpleAddEditModal from '@/components/Modals/SimpleAddEditModal.vue';

// Modules
import getAllProducts from '@/modules/product/getAllProducts';

// Variables for inits
const { products, error, load } = getAllProducts(); // change this later to "getAllInventory()"
const inventoryData = ref(null);
const legends = [
    { id: 'skuid', text: 'SKU ID' },
    { id: 'name', text: 'Product Name' },
    { id: 'category', text: 'Category' },
    { id: 'price', text: 'Price' },
    { id: 'actions', text: 'Actions' },
];
// const legends = [
//     { id: 'skuid', text: 'SKU ID' },
//     { id: 'name', text: 'Product Name' },
//     { id: 'quantity', text: 'Quantity' },
//     { id: 'actions', text: 'Actions' },
// ];
const rows = ref([]); // Used for table rows
// Do see the SimpleAddEditModal.vue for field object
const modalAddEditFields = [ // Change this later to inventory
    { id: 1, type: 'text',  hintText: 'SKU ID*' },
    { id: 2, type: 'text',  hintText: 'Product Name*' },
    { id: 3, type: 'dropdowntext',  hintText: 'Category*' },
    { id: 4, type: 'text',  hintText: 'Price*' },
];

// Variables for Child
const isOverlayCalled = ref(false);
const modalType = ref(null); // String
const modalModelValues = ref([
    { id: 1, value: '' },
    { id: 2, value: '' },
    { id: 3, value: '' },
    { id: 4, value: '' },
]);
const activeTableRow = ref(null);

// Load data after mount
onMounted(async () => {
    await load();
    
    if (error.value === null) {
        // Change all this later
        inventoryData.value = products.value;
        console.log(inventoryData.value); // Use for debug

        // Iterates over the given array
        inventoryData.value.forEach(data => {
            let newItem = [];
            let length = Object.keys(data).length

            // Get all values from the data
            Object.values(data).forEach(value => {
                newItem.push(value);
            });

            rows.value.push(newItem); // Add values as rows
        });

        console.log(rows.value); // Use for debug
    } else {
        // If possible, add a catcher
    };
});

// Variables for children
const btnAddIconColor = ref("#FFFAFA");

// Function Appearances
function changeButtonAddIconColor() {
    btnAddIconColor.value = btnAddIconColor.value === '#FFFAFA' ? '#C84A46' : '#FFFAFA';
};

function reinitializeModalVariables() {
    isOverlayCalled.value = false;
    modalType.value = null;

    modalModelValues.value.forEach(item => {
        item.value = '';
    });
};

// Function Handlers
function handleNewItemRequest() {
    isOverlayCalled.value = true;
    modalType.value = 'add'
    activeTableRow.value = null;
};

function handleTableRowEdit(rowID) {
    const row = rows.value[rowID];
    
    activeTableRow.value = rowID;
    isOverlayCalled.value = true;
    modalType.value = 'edit';

    modalModelValues.value.forEach((item, index) => {
        item.value = row[index];
    });
};
</script>

<style scoped>
#inventory {
    width: 100%;
    position: relative;
}

#header {
    margin-bottom: 50px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

#header h1 {
    color: var(--color-secondary);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>