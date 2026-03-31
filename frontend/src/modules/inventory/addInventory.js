import { ref } from 'vue';

const addInventoryItem = (newItem) => {

    const error = ref(null);
    console.log(newItem);

    const onSubmit = async () => {
        try {
            const response = await fetch(`http://localhost:8000/api/inventory/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    quantity: newItem.quantity,
                    details: newItem.details,
                    product_id: newItem.product_id
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
        } catch (err) {
            error.value = err.message;
            alert(error.value);
            console.error(err.message);
        }
    }

    return { error, onSubmit };
}

export default addInventoryItem;