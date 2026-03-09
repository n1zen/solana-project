<template>
    <header>
        <div class="logo-container">
            <h1>Solana Manager</h1>
        </div>
        <div class="nav-container">
            <nav>
                <router-link to="/">Home</router-link>
                <router-link to="/products">Products</router-link>
            </nav>
            <button>
                <MoonIcon
                    color="var(--text)"
                />
            </button>
        </div>
    </header>
</template>

<script>
import { MoonIcon } from 'lucide-vue-next';
export default {
    components: {
        MoonIcon,
    }
}
</script>

<style scoped>
    header {
        display: flex;
        justify-content: space-between;
        margin: 0 var(--space-12);
        padding-top: var(--space-2);
    }
    h1 {
        font-size: var(--text-xl)
    }
    .nav-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    nav a {
        text-decoration: none;
        color: var(--text);
        margin: 0 var(--space-4);
    }
    nav a:hover {
        color: var(--primary);
    }
    button {
        background: var(--bg-light);
        cursor: pointer;
        padding: var(--space-2) var(--space-3);
        border-radius: var(--radius-2xl);
        border: var(--border-card);
        box-shadow: var(--shadow);
        display: flex;
        align-items: center;
        justify-content: center;
    }
    button:hover {
        background: var(--gradient);
    }
</style>