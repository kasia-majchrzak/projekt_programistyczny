from PreprocessingService import PreprocessingService

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vehicula erat vitae efficitur ultrices. Fusce elementum eros in dui auctor finibus. Morbi blandit scelerisque ligula a scelerisque. Duis ac vehicula velit, pellentesque maximus neque. Suspendisse in augue felis. Curabitur vitae velit vehicula, eleifend ex a, varius felis. Nulla rhoncus, justo eget rhoncus finibus, ex felis placerat odio, id ultrices sapien justo ut diam. Ut efficitur turpis sed nulla condimentum, nec scelerisque lectus lobortis. Sed accumsan, est at elementum faucibus, tellus sem porttitor tellus, at blandit magna ipsum vitae felis. Maecenas egestas, erat sit amet sollicitudin gravida, ex massa maximus metus, id tincidunt augue eros id leo. Fusce commodo metus eu gravida finibus. Quisque vitae malesuada erat. In nec commodo ipsum, sit amet venenatis nisl. Praesent ullamcorper facilisis aliquam. Fusce quis luctus purus. Curabitur dignissim leo ex, sed eleifend sapien pretium varius. Ut dapibus tortor sed maximus congue. Donec nec interdum odio. Donec sagittis ultricies orci, nec vestibulum dolor tincidunt quis. Fusce metus ante, pharetra quis dapibus at, molestie a neque. Nullam auctor ullamcorper odio, et sollicitudin urna tincidunt ut. Vivamus vitae ultrices turpis. Nam cursus convallis lectus, et condimentum massa auctor sed. Sed pretium scelerisque odio, non blandit ligula vestibulum ac. Pellentesque facilisis, velit id rhoncus posuere, orci augue ullamcorper augue, non posuere arcu sem in odio. " \
        "Suspendisse velit mi, congue a metus id, fringilla sagittis elit. Curabitur eget commodo justo. Donec a nisl tellus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla venenatis erat vitae dolor maximus commodo.Proin fermentum quam ullamcorper felis luctus aliquet. Nullam ut orci ac mauris viverra consequat sed ac orci. Morbi vel massa in mi ullamcorper commodo. Vestibulum vel eros consequat, sollicitudin risus nec, porttitor velit. Duis maximus purus ac sapien ornare, id vehicula felis commodo. Praesent id elit blandit, viverra nulla eu, viverra dolor. Praesent in aliquam mauris, in condimentum tellus.Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Phasellus varius lobortis nisi elementum faucibus. Proin pretium, nisl quis rhoncus pretium, nisl purus mollis tellus, et commodo elit neque non tellus. Aliquam porttitor facilisis lorem. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aenean ac risus sit amet turpis consequat scelerisque non sed sapien. Cras faucibus viverra risus, nec egestas felis sodales nec. Donec consequat, mi eget eleifend elementum, dui purus rhoncus ipsum, vel vehicula magna erat ac tortor. Cras efficitur dignissim ligula suscipit porta. Mauris venenatis, nunc vel consectetur egestas, felis tortor viverra nunc, eu egestas est tortor et nulla. Donec a massa ultrices, elementum augue eu, varius dolor."

service = PreprocessingService()
service.preprocess_text(lorem)