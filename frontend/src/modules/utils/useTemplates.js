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
                productsku: data.product.sku,
                productname: data.product.name,
                rowIndex
            };

            rowTemplate = inventoryTemplate;
        };

        return rowTemplate;
    };

    return {
        tableRowTemplates
    };
};

export default Templates;