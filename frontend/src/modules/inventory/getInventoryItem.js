// fetch all products from local backend server
import { ref } from 'vue';

const getInventory = () => {

    const inventory = ref([]);
    const error = ref(null);

    const load = async () => {
        try {
            let response = await fetch(`${process.env.VUE_APP_API_URL}/api/inventory`);
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

export default getInventory;
