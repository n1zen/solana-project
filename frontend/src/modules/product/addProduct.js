import { ref } from 'vue';

const addProduct = (newItem) => {

    const error = ref(null);

    const onSubmit = async () => {
        console.log(newItem);
        try {
            const response = await fetch(`http://localhost:8000/api/products`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    sku: newItem.sku,
                    name: newItem.name,
                    category: newItem.category,
                    price: newItem.price
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
        } catch (err) {
            error.value = err.message;
            alert(error.value);
            console.error(err.message);
        }
    }

    return { error, onSubmit };
}

export default addProduct;