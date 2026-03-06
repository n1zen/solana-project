<template>
  <div class="home">
    Home Page
  </div>
  <!-- view of all products -->
  <div v-for="product in products" :key="product.id">
    {{ product.name }}
  </div>
</template>

<script>
// @ is an alias to /src
import getProducts from '@/composables/getProducts.js';

export default {
  name: 'HomeView',
  components: {
  },
  setup() {
    // on mount, show all products on a card
    const { products, error, load } = getProducts()

    load();

    return { products, error };
  }
}
</script>
