<template>
  <div class="outerbox">
    <div class="btn-group">
      <div class="btn btn-member" style="width: 200px">{{username}}</div>
      <div class="btn btn-member" style="width: 40px" v-on:click="remove"><fa icon="times" /></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'group-member',
  data () {
    return {
    };
  },
  props: {
    username: String
  },
  methods: {
    remove() {
      this.$emit("remove", this.username);
    },
  },
  components: {
  },
  created() {
  },
};
</script>

<style>
.outerbox {
  margin-bottom: 5px;
}

.btn-member {
  color: #212529;
  background-color: #EBE6EB;
  border-color: #BEB4BE;
}

.btn-member:hover,
.btn-member:focus,
.btn-member:active,
.btn-member.active,
.open .dropdown-toggle.btn-member {
  color: #212529;
  background-color: #BEB4BE;
  border-color: #BEB4BE;
}

.btn-member.disabled {
  background-color: #EBE6EB;
  border-color: #BEB4BE;
}

.btn-member .badge {
  color: #EBE6EB;
  background-color: #212529;
}
</style>
