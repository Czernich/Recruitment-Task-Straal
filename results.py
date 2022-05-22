def get_last_users_report(results_list , app):
    ids = []
    for i in range(len(results_list)):
        ids.append(results_list[i].customer_id)
    ids = list(set(ids))

    reversed_results_list = results_list[::-1]
    for i in range(len(reversed_results_list)):
        if len(ids) != 0:
            if reversed_results_list[i].customer_id in ids:
                app.last_user_report.append(reversed_results_list[i])
                ids.remove(reversed_results_list[i].customer_id)
        else:
            break
    
    return app.last_user_report