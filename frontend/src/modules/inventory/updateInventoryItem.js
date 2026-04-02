import { ref } from 'vue';

const updateInventoryItem = (inventoryItem) => {

    const error = ref(null);

    const onSubmit = async () => {
        try {
            const response = await fetch(`http://localhost:8000/api/inventory/${ inventoryItem.id }`, {
                method: 'PATCH',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(inventoryItem)
            });

            if (!response.ok) {
                const data = await response.json();
                const message = typeof data.detail === 'string'
                    ? data.detail
                    : data.detail.map(e => e.msg).join(', ');
                throw Error(message);
            }

            return response.json();
        } catch (err) {
            error.value = err.message;
            console.error(err.message);
        }
    }

    return { error, onSubmit };
}

export default updateInventoryItem;
