const DataTypeChecker = () => {
    const isNumeric = (value) => {
        return value.trim() !== '' && !isNaN(Number(value));
    };

    return {
        isNumeric
    };
};

export default DataTypeChecker;