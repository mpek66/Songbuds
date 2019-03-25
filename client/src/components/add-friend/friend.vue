<template>
  <div class="outside"
    v-bind:class="{ 'ingroup': ingroup, 'not-ingroup': (ingroup == false) }">
    <h4 class="name">{{username}}
      <span class="action btn"
        v-on:click="toggle">
        <fa icon="times" v-if="ingroup"/>
        <fa icon="plus" v-else/>
      </span>
    </h4>
  </div>
</template>

<script>
export default {
  name: 'friend',
  data() {
    return {
      username: "hello",
      ingroup: false,
    };
  },
  props: {
  },
  methods: {
    toggle() {
      if (!this.ingroup) {
        this.$emit("add", this.username);
        this.ingroup = true;
      } else {
        this.$emit("remove", this.username);
        this.ingroup = false;
      }
    }
  },
  components: {
  },
  created() {
  },
  beforeDestroy() {
  },
};
</script>

<style>
.outside {
  width: 100%;
  height: 40px;
}

.not-ingroup {
  border: solid 1px rgb(240,240,240);
  background-color: white;
}

.ingroup {
  border: solid 1px rgb(190,180,190);
  background-color: rgb(235,230,235);
}

.name {
  margin-left: 40px;
  margin-top: 5px;
  margin-bottom: 5px;
  height: 30px;
}

.action {
  float: right;
  margin-top: -6px;
  border-radius: 0px;
  height: 40px;
  width: 40px;
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
