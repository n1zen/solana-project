import { ref } from 'vue';

const addProduct = (newItem) => {

    const error = ref(null);

    const onSubmit = async () => {
        try {
            const response = await fetch(`http://localhost:8000/api/products/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(newItem)
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
            console.log(error.value);
            // alert(error.value);
            console.error(err.message);
        }
    }

    return { error, onSubmit };
}

export default addProduct;