// fetch all products from local backend server
import { ref } from 'vue';

const getAllProducts = () => {

    const products = ref([]);
    const error = ref(null);

    const load = async () => {
        try {
            let response = await fetch(`http://localhost:8000/api/products`);
            if (!response.ok) {
                throw Error('No product available')
            }
            products.value = await response.json();
        } catch (err) {
            error.value = err.message;
            console.log(error.value);
        }
    }

    return { products, error, load };
}

export default getAllProducts;