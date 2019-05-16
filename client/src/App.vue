<template>
  <div id="app">
    <navigation></navigation>
    <router-view/>
  </div>
</template>

<script>
import Navigation from '@/common/navigation/navigation';

export default {
  name: 'app',
  components: {
    "navigation": Navigation,
  }
};
</script>

<style>
#app {

}
</style>
