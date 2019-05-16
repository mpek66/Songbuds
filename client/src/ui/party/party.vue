<template>
  <div style="height: 100vh; width: 100vw; overflow: hidden">
    <div class="party-background d-flex justify-content-center">
      <div class="main">
        <party-info v-if="partyActive == false"></party-info>
        <div v-if="partyActive == true">hello</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import PartyInfo from './party-info';

export default {
  name: 'party',
  data() {
    return {
      partyActive: false,
    };
  },
  methods: {
  },
  components: {
    'party-info': PartyInfo,
  },
  created() {
    if(!this.$session.exists()){
      //this.$router.push("/login");
    }
  },
  beforeDestroy() {
  },
  watch: {
  }
};
</script>

<style>
.party-background {
  background-color: rgb(250,250,250);
  position: fixed;
  top: 50px;
  left: 0px;
  height: calc(100% - 50px);
  width: calc(100vw);
  overflow-y: wrap;
  padding: 50px;
}

.main {
  width: calc(66vw);
}
</style>
