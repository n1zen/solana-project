// fetch all inventory
import { ref } from 'vue';

const getAllInventory = () => {

    const inventory = ref([]);
    const error = ref(null);

    const load = async () => {
        try {
            let response = await fetch(`http://localhost:8000/api/inventory`);
            if (!response.ok) {
                throw Error('No inventory items available')
            }
            inventory.value = await response.json();
        } catch (err) {
            error.value = err.message;
            console.log(error.value);
        }
    }

    return { inventory, error, load };
}

export default getAllInventory;