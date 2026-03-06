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
    .card {
        border: 1px solid #ccc;
        padding: 10px;
        margin: 10px;
        border-radius: 5px;
        background-color: #f9f9f9;
    }
</style>