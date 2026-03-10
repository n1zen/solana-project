<template>
    <header>
        <div class="logo-container">
            <h1>Solana Manager</h1>
        </div>
        <div class="nav-container">
            <nav>
                <router-link to="/">Home</router-link>
                <router-link to="/products">Products</router-link>
                <router-link to="/inventory">Inventory</router-link>
            </nav>
            <button @click="toggleTheme">
                <MoonIcon
                    v-if="isDark"
                    color="var(--text)"
                />
                <SunIcon 
                    v-else
                    color="var(--text)"
                />
            </button>
        </div>
    </header>
</template>

<script>
import { MoonIcon, SunIcon } from 'lucide-vue-next';
import { ref, watch } from 'vue';
export default {
    components: {
        MoonIcon,
        SunIcon
    },
    setup() {
        const isDark = ref(false)
        // toggle light/dark mode
        const toggleTheme = () => {
            isDark.value = !isDark.value
        }

        watch(isDark, (dark) => {
            document.documentElement.setAttribute('data-theme', dark ? 'dark' : 'light')
        }, { immediate: true })
        return { isDark, toggleTheme }
    }
}
</script>

<style scoped>
    header {
        display: flex;
        justify-content: space-between;
        padding: var(--space-2) var(--space-24);
        background: var(--bg);
        border-bottom: var(--border-card);
        box-shadow: var(--shadow);
    }
    h1 {
        font-size: var(--text-xl);
        color: var(--logo);
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
        cursor: pointer;
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
        background: var(--gradient-hover);
    }
</style>