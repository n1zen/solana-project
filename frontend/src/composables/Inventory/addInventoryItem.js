import { ref } from 'vue';

const addInventoryItem = (loadInventory) => {

    const product_id = ref(null);
    const details = ref('');
    const quantity = ref(null);
    const error = ref(null);

    const onSubmit = async () => {
        try {
            const response = await fetch(`${process.env.VUE_APP_API_URL}/api/inventory`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    quantity: quantity.value,
                    details: details.value,
                    product_id: product_id.value
                })
            });

            if (!response.ok) {
                const data = await response.json();
                const message = typeof data.detail === 'string'
                    ? data.detail
                    : data.detail.map(e => e.msg).join(', ');
                throw Error(message);
            }

            alert('Inventory item added successfully');
            // refresh the product list & clear the form
            await loadInventory();
            product_id.value = null;
            details.value = '';
            quantity.value = null;
        } catch (err) {
            error.value = err.message;
            alert(error.value);
            console.error(err.message);
        }
    }

    return { product_id, details, quantity, error, onSubmit };
}

export default addInventoryItem;
