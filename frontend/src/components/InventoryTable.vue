<template>
    <table>
        <thead>
            <tr>
                <th>SKU</th>
                <th>Name</th>
                <th>Quantity</th>
                <th>Details</th>
                <th>Date Updated</th>
            </tr>
        </thead>
        <tbody>
            <tr v-if="inventory.length === 0">
                <td colspan="5">No Products Found</td>
            </tr>
            <tr v-for="inventory_item in inventory" :key="inventory_item.id">
                <td>{{ inventory_item.product.sku }}</td>
                <td>{{ inventory_item.product.name }}</td>
                <td>{{ inventory_item.quantity }}</td>
                <td>{{ inventory_item.details }}</td>
                <td>{{ formatDate(inventory_item.date_updated) }}</td>
            </tr>
        </tbody>
    </table>
</template>

<script>
import { useFormat } from '@/composables/useFormat.js'
export default {
    
    props: ['inventory'],
    setup() {
        const { formatDate } = useFormat();
        return { formatDate }
    }
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