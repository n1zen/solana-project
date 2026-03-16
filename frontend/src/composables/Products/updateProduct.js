import { ref } from 'vue';
import { useRouter } from 'vue-router';

const updateProduct = (product) => {

    const router = useRouter();
    const sku = ref(product.sku);
    const name = ref(product.name);
    const category = ref(product.category);
    const price = ref(product.price);
    const error = ref(null);

    const onSubmit = async () => {
        try {
            const response = await fetch(`${process.env.VUE_APP_API_URL}/api/products/` + product.id, {
                method: 'PATCH',
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

            alert('Product edited successfully');
            // redirect to ProductsView
            router.push({name: 'products'});
        } catch (err) {
            error.value = err.message;
            alert(error.value);
            console.error(err.message);
        }
    }

    return { sku, name, category, price, error, onSubmit };
}

export default updateProduct;
