import { ref } from 'vue';
import { useRouter } from 'vue-router';
const deleteProduct = (id) => {

    const delError = ref(null);
    const router = useRouter();

    const onDelete = async () => {
        try {
            const response = await fetch(`${process.env.VUE_APP_API_URL}/api/products/` + id, {
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

            alert('Product deleted successfully');
            router.push({ name: 'products' });
        } catch (err) {
            error.value = err.message;
            alert(error.value);
            console.error(err.message);
        }
    }

    return { delError, onDelete };
}

export default deleteProduct;