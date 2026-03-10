export function useFormat() {

    function formatDate(dateString) {
        return new Date(dateString).toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
        })
    }

    function formatCurrency(amount) {
        return `₱${amount.toLocaleDateString('en-PH')}`
    }

    return { formatDate, formatCurrency }
}