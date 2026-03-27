import { ref } from 'vue';

const updateProduct = (updatedProduct) => {

    const error = ref(null);

    const onSubmit = async () => {
        try {
            const response = await fetch(`http://localhost:8000/api/products/${ updatedProduct.id }`, {
                method: 'PATCH',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(updatedProduct)
            });

            if (!response.ok) {
                const data = await response.json();
                const message = typeof data.detail === 'string'
                    ? data.detail
                    : data.detail.map(e => e.msg).join(', ');
                throw Error(message);
            }

            // alert('Product edited successfully');
        } catch (err) {
            error.value = err.message;
            // alert(error.value);
            console.error(err.message);
        }
    }

    return { error, onSubmit };
}

export default updateProduct;
