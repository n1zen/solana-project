<template>
    <table>
        <thead>
            <tr>
                <th>SKU</th>
                <th>Name</th>
                <th>Category</th>
                <th>Price</th>
            </tr>
        </thead>
        <tbody>
            <tr v-if="products.length === 0">
                <td colspan="4">No Products Found</td>
            </tr>
            <tr v-for="product in products" :key="product.id">
                <td>{{ product.sku }}</td>
                <td>{{ product.name }}</td>
                <td>{{ product.category }}</td>
                <td>{{ product.price }}</td>
            </tr>
        </tbody>
    </table>
</template>

<script>
export default {
    props: ['products'],
}
</script>

<style scoped>
table {
    background: var(--gradient);
    padding: var(--space-4) var(--space-6);
    margin: var(--space-6);
    border-radius: var(--radius-md);
    border: var(--border-card);
    border-top: var(--highlight);
    box-shadow: var(--shadow);
    text-align: center;
}
table:hover {
    background: var(--gradient-hover);
}
th {
    background: var(--bg-light);
}
th:first-child {
    border-top-left-radius: var(--radius-md);
}
th:last-child {
    border-top-right-radius: var(--radius-md);
}
th, td {
    padding: var(--space-2) var(--space-4);
    border: var(--border-card);
    box-shadow: var(--shadow);
}
td {
    background: var(--bg-dark);
}
tr:last-child td:last-child {
    border-bottom-right-radius: var(--radius-md);
}
tr:last-child td:first-child {
    border-bottom-left-radius: var(--radius-md);
}
</style>