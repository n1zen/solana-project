<template>
    <div class="card">
        <h3>{{ product.name }}</h3>
        <p>Category: {{ product.category }}</p>
        <p>Php {{ product.price }}</p>
    </div>
</template>

<script>
    export default {
        props: ['product']
    }
</script>

<style scoped>

</style>