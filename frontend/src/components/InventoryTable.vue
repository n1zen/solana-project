<template>
    <table>
        <thead>
            <tr>
                <th>SKU</th>
                <th>Name</th>
                <th>Quantity</th>
                <th>Date Updated</th>
            </tr>
        </thead>
        <tbody>
            <tr v-if="inventory.length === 0">
                <td colspan="4">No Products Found</td>
            </tr>
            <tr v-for="inventory_item in inventory" :key="inventory_item.id">
                <td>{{ inventory_item.product.sku }}</td>
                <td>{{ inventory_item.product.name }}</td>
                <td>{{ inventory_item.quantity }}</td>
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
</style>