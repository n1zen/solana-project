const Templates = () => {

    const tableRowTemplates = (type, rowIndex, data) => {
        let rowTemplate = {};

        if (type === 'product') {
            let productTemplate = {
                sku: data.sku,
                name: data.name,
                category: data.category,
                price: data.price,
                id: data.id,
                rowIndex
            };

            rowTemplate = productTemplate;
        } else if (type === 'inventory') {
            let inventoryTemplate = {
                quantity: data.quantity,
                details: data.details,
                id: data.id,
                product_sku: data.product.sku,
                product_name: data.product.name,
                rowIndex
            };

            rowTemplate = inventoryTemplate;
        };

        return rowTemplate;
    };

    const messageTemplates = (type, messageType, data, key) => {
        let messageTemplate = {}

        if (type === 'product') {
            const messageTemplates = {
                add: `Product ${ data[key] } has been added successfully!`,
                edit: `Product ${ data[key] } has been updated successfully!`,
                delete: `Product ${ data[key] } has been deleted successfully!`
            }

            messageTemplate = messageTemplates[messageType];
        } else if (type === 'inventory') {
            const messageTemplates = {
                add: `Product ${ data[key] } has been added to inventory!`,
                edit: `Product ${ data[key] } has been updated successfully!`,
                delete: `Product ${ data[key] } has been deleted from the inventory!`
            }

            messageTemplate = messageTemplates[messageType];
        }

        return messageTemplate;
    };

    return {
        tableRowTemplates,
        messageTemplates
    };
};

export default Templates;