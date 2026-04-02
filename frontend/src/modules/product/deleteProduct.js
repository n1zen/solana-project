import { ref } from 'vue';
const deleteProduct = (id) => {

    const error = ref(null);

    const onDelete = async () => {
        try {
            const response = await fetch(`http://localhost:8000/api/products/${id}`, {
                method: 'DELETE',
                headers: { 'Content-Type': 'application/json' }
            });

            if (!response.ok) {
                const data = await response.json();
                const message = typeof data.detail === 'string'
                    ? data.detail
                    : data.detail.map(e => e.msg).join(', ');
                throw Error(message);
            }

            console.log(response.json());
            // alert('Product deleted successfully');
        } catch (err) {
            error.value = err.message;
            // alert(error.value);
            console.error(err.message);
        }
    }

    return { error, onDelete };
}

export default deleteProduct;