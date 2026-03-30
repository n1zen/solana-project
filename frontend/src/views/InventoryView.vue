<template>
    <transition name="fade">
        <Overlay
            v-if="isOverlayCalled"
            @on-click=""
            >
            <template>
                <transition name="fade">
                    
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
                        @on-click="handleAddRequest"
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
const rows = ref([]);

// Variables for Child
const isOverlayCalled = ref(false);
const modalType = ref(null); // String

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

// Function Handlers

function changeButtonAddIconColor() {
    btnAddIconColor.value = btnAddIconColor.value === '#FFFAFA' ? '#C84A46' : '#FFFAFA';
};

function handleAddRequest() {

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