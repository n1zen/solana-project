import { ref } from "vue";

import getAllProducts from "../product/getAllProducts";
import getAllInventory from "../inventory/getAllInventory";

/**
 * 
 * @param {String} type - The type of items to be received. Example: 'product', 'inventory', 'order'
 */
const Search = (type) => {

    const dataFromServer = ref([]);
    const getModules = {
        product: (() => {
            const m = getAllProducts();
            return {
                data: m.products,
                load: m.load,
                error: m.error
            };
        })(),
        inventory: (() => {
            const m = getAllInventory();
            return {
                data: m.inventory,
                load: m.load,
                error: m.error
            };
        })()
    };

    loader();

    async function loader() {
        const module = getModules[type];
        if (!module) return;

        const { data, load, error } = module;

        await load();

        if (error.value === null) {
            dataFromServer.value = data.value;
        } else {
            // add catcher
            console.log(error.value);
        };
    };

    /**
     * @param { String } id - The id to be searched  
     */
    const searchById = (id) => {
        const data = dataFromServer.value;

        const searchConfig = {
            product: {
                getId: (datum) => datum.sku,
                getName: (datum) => datum.name
            },
            inventory: {
                getId: (datum) => datum.product?.sku,
                getName: (datum) => datum.product?.name
            },
            // orders: {
            //     getId: (datum) => datum.order_number,
            //     getName: (datum) => datum.customer_name
            // }
        };

        const config = searchConfig[type];
        if (!config) return;

        for (const datum of data) {
            if (config.getId(datum) == id) return config.getName(datum);
        };
    };

    return {
        searchById
    };
};

export default Search;