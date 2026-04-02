import { ref } from "vue";

import getAllProducts from "../product/getAllProducts";
import getAllInventory from "../inventory/getAllInventory";

/**
 * 
 * @param {String} type - The type of items to be received. Example: 'product', 'inventory', 'order'
 */
const SearchItem = (type) => {

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

    const refreshSearchData = async () => await loader();

    const searchConfig = {
        product: {
            all: (datum) => datum,
            id: (datum) => datum.sku,
            name: (datum) => datum.name,
            category: (datum) => datum.category,
            price: (datum) => datum.price,
        },
        
        inventory: {
            all: (datum) => datum,
            id: (datum) => datum.product?.sku,
            name: (datum) => datum.product?.name,
            category: (datum) => datum.product?.category,
            quantity: (datum) => datum.quantity
        },

        // orders: {
        //     all: (datum) => datum
        //     id: (datum) => datum.order_number,
        //     name: (datum) => datum.customer_name,
        // }
    };

    /**
     * Search inside dataFromServer depending on current type
     * 
     * @param {Object} params
     * @param {'id' | 'name' | 'category'} params.searchBy - Field used to search
     * @param {String|Number} params.value - Value to search
     * @param {String} [params.returnField='all'] - Field to return
     * @returns {*}
     */
    const searchData = ({ searchBy, value, returnField = 'all' }) => {
        const data = dataFromServer.value;
        const config = searchConfig[type];

        if (!config) return;
        if (!config[searchBy]) return;
        if (!config[returnField]) return;

        const foundItem = data.find((datum) => config[searchBy](datum) == value);

        if (!foundItem) return;

        return config[returnField](foundItem);
    };

    /**
     * @param {String|Number} id
     * @param {String} [returnField='all']
     * @returns {*}
     */
    const searchById = (id, returnField = 'all') => {
        return searchData({
            searchBy: 'id',
            value: id,
            returnField
        });
    };

    /**
     * @param {String} name
     * @param {String} [returnField='all']
     * @returns {*}
     */
    const searchByName = (name, returnField = 'all') => {
        return searchData({
            searchBy: 'name',
            value: name,
            returnField
        });
    };

    /**
     * Search multiple matching items
     * 
     * @param {Object} params
     * @param {'id' | 'name'} params.searchBy - Field used to search
     * @param {String|Number} params.value - Value to search
     * @param {'item' | 'id' | 'name' | 'price' | 'category'} [params.returnField='item'] - Value to return
     * @param {'exact' | 'startsWith' | 'includes'} [params.matchType='exact'] - Matching method
     * @returns {Array}
     */
    const searchMany = ({ searchBy, value, returnField = 'item', matchType = 'exact' }) => {
        const data = dataFromServer.value;
        const config = searchConfig[type];

        if (!config) return [];
        if (!config[searchBy]) return [];
        if (!config[returnField]) return [];

        return data
            .filter((datum) => {
                const fieldValue = config[searchBy](datum);

                if (fieldValue === undefined || fieldValue === null) return false;

                const normalizedField = String(fieldValue).toLowerCase();
                const normalizedValue = String(value).toLowerCase();

                if (matchType === 'exact') {
                    return normalizedField === normalizedValue;
                }

                if (matchType === 'startsWith') {
                    return normalizedField.startsWith(normalizedValue);
                }

                if (matchType === 'includes') {
                    return normalizedField.includes(normalizedValue);
                }

                return false;
            })
            .map((datum) => config[returnField](datum));
    };


    return {
        refreshSearchData,
        searchById,
        searchByName,
        searchMany
    };
};

export default SearchItem;