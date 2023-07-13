function AjaxReq(dataList) {
  let csrfToken = document.querySelector(
    'input[name="csrfmiddlewaretoken"]',
  ).value
  var maxVal = document.getElementById('product_quantity')

  $.ajax({
    type: 'POST',
    url: '',
    data: JSON.stringify(dataList),
    headers: {
      'Content-type': 'application/json',
      'X-CSRFToken': csrfToken,
    },
    success: function (response) {
      maxVal.max = response.quantity
      $('#offer').html(response.offer)
      $('#price').html(response.price)
      $('#discount_price').html(response.discount_price)
      $('#offer_duration').html(response.offer_duration)
      $('#quantity').html(response.quantity)
      if (Number.isInteger(response.quantity)) {
        $('#button').prop('disabled', false)
      } else {
        $('#button').prop('disabled', true)
      }
    },
  })
}
function singleProductAjax() {
  const selectElements = document.querySelectorAll('select')
  const selectDataList = []

  selectElements.forEach((select) => {
    const selectData = {
      name: select.name,
      id: select.id,
      value: select.value,
    }
    selectDataList.push(selectData)
    console.log(selectElements.length > 0)

    select.addEventListener('change', () => {
      selectData.value = select.value
      AjaxReq(selectDataList)
    })
  })
}
