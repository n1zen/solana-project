// fetch all inventory from local backend server
import { ref } from 'vue';

const getAllProducts = () => {

    const inventory = ref([]);
    const error = ref(null);

    const load = async () => {
        try {
            let response = await fetch('http://localhost:8000/api/inventory/');
            if (!response.ok) {
                throw Error('No product available')
            }
            inventory.value = await response.json();
        } catch (err) {
            error.value = err.message;
            console.log(error.value);
        }
    }

    return { inventory, error, load };
}

export default getAllProducts;