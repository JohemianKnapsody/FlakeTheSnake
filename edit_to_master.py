            elif c in ['h']:
                stage.move_rel( [1,0,0] * step_param.value)
                n = 0
                count = 0
                while count < 10:
                    while os.path.isfile(os.path.join(filepath % n)):
                        n += 1
                    camera.capture(filepath % n, format="jpeg", bayer=True)
                    camera.annotate_text="Saved '%s'" % (filepath % n)
                    time.sleep(0.5)
                    camera.annotate_text=""
                    count+=1
