function singleProductAjax() {
  const selectElements = document.querySelectorAll('select')
  const selectDataList = []
  var maxVal = document.getElementById('product_quantity')

  let csrfToken = document.querySelector(
    'input[name="csrfmiddlewaretoken"]',
  ).value

  selectElements.forEach((select) => {
    const selectData = {
      name: select.name,
      id: select.id,
      value: select.value,
    }
    if (selectData.name != '') {
      selectDataList.push(selectData)
    }

    select.addEventListener('change', () => {
      selectData.value = select.value

      $.ajax({
        type: 'POST',
        url: '',
        data: JSON.stringify(selectDataList),
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
    })
  })
}
