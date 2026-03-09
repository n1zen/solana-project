<template>
  <!-- Header -->
  <Header />
  <!-- Body   -->
  <router-view/>
  <!--Footer  -->
</template>

<script>
import Header from '@/components/Header.vue';
export default {
  components: {
    Header,
  }
}
</script>