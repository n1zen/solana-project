<template>
    <div class="card">
        <div class="title">
            <p class="sku">SKU: {{ product.sku }}</p>
            <h3 class="name">{{ product.name }}</h3>
        </div>
        <div class="content-actions">
            <div class="content">
                <p class="category">Category: {{ product.category }}</p>
                <p class="price">₱{{ product.price }}</p>
            </div>
            <div class="actions">
                <button class="edit">
                    <PenLineIcon size="var(--text-base)"/>
                </button>
                <button class="delete">
                    <Trash2Icon size="var(--text-base)"/>
                </button>
            </div>
        </div>
    </div>
</template>

<script>
    import { PenLineIcon, Trash2Icon } from 'lucide-vue-next'
    export default {
        components: {
            PenLineIcon,
            Trash2Icon
        },
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
        width: 45%;
        margin: var(--space-6) 0;
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
    .content-actions {
        display: flex;
        justify-content: space-between;
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
    .actions {
        display: flex;
        justify-content: center;
        align-items: end;
    }
    button {
        margin: 0 var(--space-1) var(--space-4) var(--space-1);
        border-radius: var(--radius-xl);
        padding: var(--space-2) var(--space-2);
        color: var(--text);
        background: var(--bg-light);
        border: var(--border-card);
        border-top: var(--highlight);
        box-shadow: var(--shadow);
        display: flex;
        justify-content: center;
        align-items: center;
    }
    button.edit:hover {
        background-color: var(--primary);
        color: var(--text-inverse);
    }
    button.edit:active {
        box-shadow: none;
        color: var(--text-inverse);
        background-color: var(--secondary);
    }
    button.delete:hover {
        background-color: var(--warning);
        color: var(--text-inverse);
    }
    button.delete:active {
        box-shadow: none;
        color: var(--text-inverse);
        background-color: var(--danger);
    }
</style>