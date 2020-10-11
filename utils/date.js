export const formatDate = (dateString) => {
  const d = new Date(dateString)

  return `${d.getDate()}.${d.getMonth()}.${d.getFullYear()}`
}