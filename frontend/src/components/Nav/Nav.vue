<template>
    <nav id="nav" class="nav">
        <div id="top">
            <div id="cont-logo">
                <div id="logo">
                    <img src="../../assets/solana_logo_15pt.avif" alt="solana_logo">
                </div>
                <div id="logo-name">
                    Solana Atelier
                </div>
            </div>
            <div id="cont-side-panel">
                <div id="cont-profile-time">
                    <div id="cont-profile-time-upper-section">
                        <img src="../../assets/photos/christina-wocintechchat-com-m-PlikkWB79qs-unsplash.jpg"
                            alt="Profile Picture" id="profile-photo">
                        <div id="date-time">
                            <span id="date">Tue, Mar. 3</span>
                            <span id="time">03:39PM</span>
                        </div>
                    </div>
                    <div id="cont-lower-section">
                        <p id="welcome">
                            Welcome back,
                            <br /><span id="user">Adrenaline</span>!
                        </p>
                    </div>
                </div>
                <div id="cont-pages">
                    <NavButton 
                        :is-selected="activeButton === 'Dashboard'"
                        :is-hovered="hoveredButton === 'Dashboard'"
                        :is-blurred="activeButton === 'Dashboard' && activeButton !== hoveredButton && hoveredButton !== null && hoveredButton !== 'Logout'" 
                        text="Dashboard" 
                        @on-hover="buttonOnHover" 
                        @on-leave="buttonOnLeave"
                        @on-click="changePage" />
                    <NavButton 
                        :is-selected="activeButton === 'Lifecycle'"
                        :is-hovered="hoveredButton === 'Lifecycle'" 
                        :is-blurred="activeButton === 'Lifecycle' && activeButton !== hoveredButton && hoveredButton !== null && hoveredButton !== 'Logout'" 
                        :icon="buttonIcons.lifecycle" text="Lifecycle" 
                        @on-hover="buttonOnHover" 
                        @on-leave="buttonOnLeave" 
                        @on-click="changePage" />
                    <NavButton 
                        :is-selected="activeButton === 'Analytics'"
                        :is-hovered="hoveredButton === 'Analytics'"
                        :is-blurred="activeButton === 'Analytics' && activeButton !== hoveredButton && hoveredButton !== null && hoveredButton !== 'Logout'" 
                        :icon="buttonIcons.analytics" text="Analytics"
                        @on-hover="buttonOnHover" 
                        @on-leave="buttonOnLeave"
                        @on-click="changePage" />
                    <NavButton 
                        :is-selected="activeButton === 'Projects'" 
                        :is-hovered="hoveredButton === 'Projects'"
                        :is-blurred="activeButton === 'Projects' && activeButton !== hoveredButton && hoveredButton !== null && hoveredButton !== 'Logout'" 
                        :icon="buttonIcons.projects" text="Projects" 
                        @on-hover="buttonOnHover" 
                        @on-leave="buttonOnLeave"
                        @on-click="changePage" />
                    <NavButton 
                        :is-selected="activeButton === 'Teams'" 
                        :is-hovered="hoveredButton === 'Teams'"
                        :is-blurred="activeButton === 'Teams' && activeButton !== hoveredButton && hoveredButton !== null && hoveredButton !== 'Logout'" 
                        :icon="buttonIcons.teams" text="Teams" 
                        @on-hover="buttonOnHover" 
                        @on-leave="buttonOnLeave"
                        @on-click="changePage" />
                    <NavButton 
                        :is-selected="activeButton === 'Inventory'" 
                        :is-hovered="hoveredButton === 'Inventory'"
                        :is-blurred="activeButton === 'Inventory' && activeButton !== hoveredButton && hoveredButton !== null && hoveredButton !== 'Logout'" 
                        :icon="buttonIcons.inventory" text="Inventory" 
                        @on-hover="buttonOnHover" 
                        @on-leave="buttonOnLeave"
                        @on-click="changePage" />
                    <NavButton 
                        :is-selected="activeButton === 'Products'" 
                        :is-hovered="hoveredButton === 'Products'"
                        :is-blurred="activeButton === 'Products' && activeButton !== hoveredButton && hoveredButton !== null && hoveredButton !== 'Logout'" 
                        :icon="buttonIcons.products" text="Products" 
                        @on-hover="buttonOnHover" 
                        @on-leave="buttonOnLeave"
                        @on-click="changePage" />
                </div>
            </div>
        </div>
        <div id="cont-logout">
            <NavButton 
                :is-hovered="hoveredButton === 'Logout'"
                :icon="buttonIcons.logout" text="Logout" textcolor="#C84A46"
                :is-logout="true"
                @on-hover="buttonOnHover" @on-leave="buttonOnLeave" />
        </div>
    </nav>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import NavButton from '@/components/Buttons/NavButton/NavButton.vue';

const router = useRouter();
const route = useRoute();

const buttonIcons = {
    lifecycle: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M7 19H4.815C4.49956 19.0009 4.18925 18.9203 3.91417 18.7659C3.63909 18.6116 3.40857 18.3887 3.245 18.119C3.08791 17.8481 3.00484 17.5407 3.00414 17.2275C3.00344 16.9144 3.08512 16.6066 3.241 16.335L7.196 9.5" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M11 19H19.203C19.5169 18.9976 19.8249 18.9144 20.0974 18.7586C20.3699 18.6027 20.5978 18.3793 20.759 18.11C20.9139 17.8399 20.9954 17.5339 20.9954 17.2225C20.9954 16.9111 20.9139 16.6051 20.759 16.335L19.533 14.215" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M14 16L11 19L14 22" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M8.293 13.596L7.196 9.5L3.1 10.598" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M9.344 5.811L10.437 3.919C10.594 3.6454 10.819 3.41701 11.0902 3.25599C11.3614 3.09497 11.6697 3.00679 11.985 3C12.2979 2.99942 12.6055 3.08116 12.8769 3.23703C13.1482 3.39289 13.3738 3.6174 13.531 3.888L17.474 10.731" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M13.378 9.63301L17.474 10.731L18.571 6.63501" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>`,
    analytics: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M3 3V19C3 19.5304 3.21071 20.0391 3.58579 20.4142C3.96086 20.7893 4.46957 21 5 21H21" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M19 9L14 14L10 10L7 13" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>`,
    projects: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M18 19C16.6739 19 15.4021 18.4732 14.4645 17.5355C13.5268 16.5979 13 15.3261 13 14V22" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M9 20H4C3.46957 20 2.96086 19.7893 2.58579 19.4142C2.21071 19.0391 2 18.5304 2 18V5C2 4.46957 2.21071 3.96086 2.58579 3.58579C2.96086 3.21072 3.46957 3 4 3H7.9C8.23449 2.99673 8.56445 3.07739 8.8597 3.23462C9.15495 3.39186 9.40604 3.62063 9.59 3.9L10.4 5.1C10.5821 5.37653 10.83 5.60353 11.1215 5.76061C11.413 5.91769 11.7389 5.99995 12.07 6H20C20.5304 6 21.0391 6.21072 21.4142 6.58579C21.7893 6.96086 22 7.46957 22 8V13" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M13 14C14.1046 14 15 13.1046 15 12C15 10.8954 14.1046 10 13 10C11.8954 10 11 10.8954 11 12C11 13.1046 11.8954 14 13 14Z" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M20 21C21.1046 21 22 20.1046 22 19C22 17.8954 21.1046 17 20 17C18.8954 17 18 17.8954 18 19C18 20.1046 18.8954 21 20 21Z" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
`,
    teams: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M19.414 14.414C21 12.828 22 11.5 22 9.49999C22 8.38719 21.6624 7.30057 21.0319 6.38366C20.4013 5.46674 19.5075 4.76265 18.4684 4.36439C17.4293 3.96613 16.2938 3.89244 15.212 4.15304C14.1301 4.41364 13.1528 4.99627 12.409 5.82399M19.414 14.414C19.2168 14.6113 18.9826 14.7677 18.7249 14.8745C18.4672 14.9813 18.191 15.0362 17.912 15.0362C17.633 15.0362 17.3568 14.9813 17.0991 14.8745C16.8414 14.7677 16.6072 14.6113 16.41 14.414C16.6235 14.6071 16.7956 14.8416 16.9157 15.1032C17.0358 15.3649 17.1015 15.6482 17.1087 15.9361C17.116 16.2239 17.0646 16.5102 16.9578 16.7775C16.851 17.0449 16.6909 17.2877 16.4873 17.4913C16.2837 17.6949 16.0409 17.855 15.7735 17.9618C15.5062 18.0686 15.2199 18.12 14.9321 18.1127C14.6443 18.1055 14.3609 18.0398 14.0993 17.9197C13.8376 17.7996 13.6031 17.6275 13.41 17.414C13.6074 17.6106 13.7641 17.8442 13.8712 18.1015C13.9782 18.3587 14.0335 18.6345 14.0339 18.9132C14.0342 19.1918 13.9797 19.4678 13.8733 19.7253C13.767 19.9828 13.6109 20.2168 13.414 20.414C13.224 20.6041 12.9976 20.7539 12.7484 20.8545C12.4991 20.9552 12.2322 21.0045 11.9635 20.9997C11.6947 20.9948 11.4297 20.9358 11.1843 20.8263C10.9389 20.7167 10.718 20.5588 10.535 20.362L5 15C3.5 13.5 2 11.8 2 9.49999C2.00022 8.38728 2.33794 7.3008 2.96856 6.38404C3.59917 5.46727 4.49303 4.76335 5.53208 4.36521C6.57112 3.96708 7.7065 3.89346 8.78826 4.15409C9.87002 4.41472 10.8473 4.99733 11.591 5.82499C11.7022 5.92833 11.8484 5.98568 12.0002 5.98549C12.152 5.98531 12.2981 5.9276 12.409 5.82399M19.414 14.414C19.7889 14.0389 19.9996 13.5303 19.9996 13C19.9996 12.4697 19.7889 11.961 19.414 11.586L17.533 9.70399C17.3092 9.48009 17.0435 9.30248 16.751 9.1813C16.4585 9.06012 16.1451 8.99775 15.8285 8.99775C15.5119 8.99775 15.1985 9.06012 14.906 9.1813C14.6135 9.30248 14.3478 9.48009 14.124 9.70399L12.414 11.414C12.0389 11.7889 11.5303 11.9996 11 11.9996C10.4697 11.9996 9.96106 11.7889 9.586 11.414C9.21106 11.0389 9.00043 10.5303 9.00043 9.99999C9.00043 9.46966 9.21106 8.96105 9.586 8.58599L12.409 5.82399" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
`,
    inventory: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12 12V9C12 8.73478 11.8946 8.48043 11.7071 8.29289C11.5196 8.10536 11.2652 8 11 8H9C8.73478 8 8.48043 8.10536 8.29289 8.29289C8.10536 8.48043 8 8.73478 8 9V12" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M16 20V17C16 16.7348 15.8946 16.4804 15.7071 16.2929C15.5196 16.1054 15.2652 16 15 16H13C12.7348 16 12.4804 16.1054 12.2929 16.2929C12.1054 16.4804 12 16.7348 12 17V20" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M20 22V2" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M4 12H20" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M4 20H20" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M4 2V22" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M4 4H20" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
`,
    products: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12 22V12" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M20.27 18.27L22 20" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M21 10.498V8.00002C20.9996 7.6493 20.9071 7.30483 20.7315 7.00119C20.556 6.69754 20.3037 6.44539 20 6.27002L13 2.27002C12.696 2.09449 12.3511 2.00208 12 2.00208C11.6489 2.00208 11.304 2.09449 11 2.27002L4 6.27002C3.69626 6.44539 3.44398 6.69754 3.26846 7.00119C3.09294 7.30483 3.00036 7.6493 3 8.00002V16C3.00053 16.3506 3.0932 16.6948 3.26871 16.9983C3.44422 17.3018 3.69641 17.5537 4 17.729L11 21.729C11.304 21.9047 11.6488 21.9973 11.9999 21.9975C12.3509 21.9977 12.6959 21.9054 13 21.73L13.98 21.171" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M3.29 7L12 12L20.71 7" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M7.5 4.27002L16.497 9.41802" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M18.5 19C19.8807 19 21 17.8807 21 16.5C21 15.1193 19.8807 14 18.5 14C17.1193 14 16 15.1193 16 16.5C16 17.8807 17.1193 19 18.5 19Z" stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
`,
    down: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M14 15L9 20L4 15" stroke="#A4D8EB" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M20 4H13C11.9391 4 10.9217 4.42143 10.1716 5.17157C9.42143 5.92172 9 6.93913 9 8V20" stroke="#A4D8EB" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
`,
    logout: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M16 17L21 12L16 7" stroke="#C84A46" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M21 12H9" stroke="#C84A46" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M9 21H5C4.46957 21 3.96086 20.7893 3.58579 20.4142C3.21071 20.0391 3 19.5304 3 19V5C3 4.46957 3.21071 3.96086 3.58579 3.58579C3.96086 3.21071 4.46957 3 5 3H9" stroke="#C84A46" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>`
};

const activeButton = ref('Dashboard'); // Dashboard as default
const hoveredButton = ref(null);

watch(route, () => {
    activeButton.value = route.name.charAt(0).toUpperCase() + route.name.slice(1);
});

// FROM CHILD EMITS
function changePage(pageName) {
    if (activeButton.value === pageName) return;

    activeButton.value = pageName;
    router.push(`/${pageName.toLowerCase()}`)
};

function buttonOnHover(buttonName) {
    hoveredButton.value = buttonName;
}

function buttonOnLeave() {
    hoveredButton.value = null;
}
</script>

<style scoped>
#nav {
    --real-width: 320px;

    height: calc(100dvh - var(--margin-top-main));
    padding-left: 50px;
    padding-bottom: var(--margin-top-main);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: sticky;
    top: calc(var(--margin-top-main));
}

#cont-logo {
    margin-bottom: 30px;
    width: var(--real-width);
    display: flex;
    align-items: center;
    gap: 17px;
}

#logo {
    aspect-ratio: 1;
    background-color: var(--color-secondary);
    border-radius: 10px;
    width: 50px;
    height: 50px;
    display: flex;
    justify-content: center;
    align-items: center;

    img {
        width: 30px;
        object-fit: contain;
    }
}

#logo-name {
    color: var(--color-secondary);
    font-family: 'SolanaAtelier', 'sans-serif';
    font-weight: bold;
    font-size: 36px;
}

#cont-side-panel {
    background-color: var(--color-secondary);
    border-radius: 15px;
    width: var(--real-width);
    padding: 20px;
}

#cont-profile-time {
    color: var(--color-primary);
    border-bottom: 2px solid var(--color-primary);
    margin-bottom: 17px;
    padding-bottom: 17px;
}

#cont-profile-time-upper-section {
    padding-bottom: 17px;
    display: flex;
    justify-content: space-between;
}

#date-time {
    text-align: right;
    display: flex;
    flex-direction: column;
}

#profile-photo {
    aspect-ratio: 1;
    border-radius: 5px;
    width: 60px;
    object-fit: cover;
}

#cont-lower-section {
    font-size: 24px;
}

#welcome {
    line-height: 30px;
}

#cont-logout {
    padding-left: 20px;
}
</style>