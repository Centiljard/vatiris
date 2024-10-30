<template>
    <div style="height: 30px; background: #666">
        <v-btn
        variant="text"
        rounded="0"
        size="small"
        :color="ESAA ? 'white' : 'grey-lighten-1'"
        @click="ESAA = !ESAA"
        >ESAA</v-btn
        >
        <v-btn
        variant="text"
        rounded="0"
        size="small"
        :color="FIR.length > 0 ? 'white' : 'grey-lighten-1'"
        @click="adFilter = ''"
        >FIRs
        <v-menu
            activator="parent"
            transition="slide-y-transition"
            :close-on-content-click="false"
            >
            <v-list density="compact">
                <v-list-item
                @click="EDWW = !EDWW"
                :class="EDWW ? '' : 'text-grey'"
                > <v-list-item-title>EDWW</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="EKDK = !EKDK"
                :class="EKDK ? '' : 'text-grey'"
                > <v-list-item-title>EKDK</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="EFIN = !EFIN"
                :class="EFIN ? '' : 'text-grey'"
                > <v-list-item-title>EFIN</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="ENOR = !ENOR"
                :class="ENOR ? '' : 'text-grey'"
                > <v-list-item-title>ENOR</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="EVRR = !EVRR"
                :class="EVRR ? '' : 'text-grey'"
                > <v-list-item-title>EVRR</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="EETT = !EETT"
                :class="EETT ? '' : 'text-grey'"
                > <v-list-item-title>EETT</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="EPWW = !EPWW"
                :class="EPWW ? '' : 'text-grey'"
                > <v-list-item-title>EPWW</v-list-item-title>
                </v-list-item>

                <v-list-item
                @click="UMKK = !UMKK"
                :class="UMKK ? '' : 'text-grey'"
                > <v-list-item-title>UMKK</v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu>
        </v-btn>
        
    </div>
    <div>
    <h1>Test</h1>
  </div>
</template>

<script setup lang="ts">
import useEventBus from "@/eventbus"
import { ref, reactive } from "vue"

const EDWW = ref(true)
const ESAA = ref(true)
const EKDK = ref(false)
const EFIN = ref(false)
const ENOR = ref(false)
const EVRR = ref(false)
const EETT = ref(false)
const EPWW = ref(false)
const UMKK = ref(false)

const FIR = reactive(["ALL"])
const adFilter = ref("")

// Set up event bus listener
const bus = useEventBus();
  bus.on("refresh", () => {
    console.log("Refresh")
  });
</script>