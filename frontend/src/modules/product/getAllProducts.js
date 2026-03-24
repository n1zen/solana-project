// fetch all products from local backend server
import { ref } from 'vue';

import testData from '../../sandbox/test.json';

const getAllProducts = () => {

    const products = ref([]);
    const error = ref(null);

    const load = async () => {
        try {
            // let response = await fetch(`${process.env.VUE_APP_API_URL}/api/products`);
            // if (!response.ok) {
            //     throw Error('No product available')
            // }
            // products.value = await response.json();
            products.value = testData;
        } catch (err) {
            error.value = err.message;
            console.log(error.value);
        }
    }

    return { products, error, load };
}

export default getAllProducts;