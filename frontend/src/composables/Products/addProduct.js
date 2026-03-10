import { ref } from 'vue';

const addProduct = (loadProducts) => {

    const sku = ref(null);
    const name = ref('');
    const category = ref('');
    const price = ref(null);
    const error = ref(null);

    const onSubmit = async () => {
        try {
            const response = await fetch(`${process.env.VUE_APP_API_URL}/api/products`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    sku: sku.value,
                    name: name.value,
                    category: category.value,
                    price: price.value
                })
            });

            if (!response.ok) {
                const data = await response.json();
                const message = typeof data.detail === 'string'
                    ? data.detail
                    : data.detail.map(e => e.msg).join(', ');
                throw Error(message);
            }

            alert('Product added successfully');
            // refresh the product list & clear the form
            await loadProducts();
            sku.value = null;
            name.value = '';
            category.value = '';
            price.value = null;
        } catch (err) {
            error.value = err.message;
            alert(error.value);
            console.error(err.message);
        }
    }

    return { sku, name, category, price, error, onSubmit };
}

export default addProduct;
