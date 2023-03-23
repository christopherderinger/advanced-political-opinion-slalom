category_groups = document.getElementsByClassName("mw-category-group")

index = 1

while(index < category_groups.length){
	li_elements = category_groups[index].children[1].children
	
	index_li = 0
	
	while(index_li < li_elements.length){
		
		console.log(li_elements[index_li].children[0].href)
		
		index_li = index_li + 1	
	}
	
	
	index = index + 1
	
}
