<template>
    <header>
        <h1>Solana Manager</h1>
        <nav>
            <router-link to="/">Home</router-link>
            <router-link to="/products">Products</router-link>
        </nav>
        <button>
            <MoonIcon/>
        </button>
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
</style>