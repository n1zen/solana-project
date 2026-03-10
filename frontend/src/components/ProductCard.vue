<template>
    <div class="card">
        <div class="title">
            <p class="sku">{{ product.sku }}</p>
            <h3 class="name">{{ product.name }}</h3>
        </div>
        <div class="content">
            <p class="category">Category: {{ product.category }}</p>
            <p class="price">₱{{ product.price }}</p>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['product']
    }
</script>

<style scoped>
    .card {
        background: var(--gradient);
        padding: var(--space-2) var(--space-4);
        border-radius: var(--radius-2xl);
        border: var(--border-card);
        box-shadow: var(--shadow);
        border-top: var(--highlight);
        width: 10rem;
        margin: var(--space-2) 0;
        flex: 0 0 calc(33.333% 0 16px);
    }
    .card:hover {
        background: var(--gradient-hover);
    }
    .sku {
        display: block;
        margin-bottom: var(--space-2);
        color: var(--text-muted);
        font-size: var(--text-sm);
    }
    .name {
        display: block;
        margin-top: 0;
        font-size: var(--text-lg);
    }
    .category {
        display: block;
        margin-bottom: var(--space-2);
        color: var(--text-muted);
        font-size: var(--text-sm);
    }
    .price {
        display: block;
        margin-top: 0;
        font-size: var(--text-lg);
        font-weight: bold;
    }
</style>